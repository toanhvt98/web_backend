from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination

User = get_user_model()


class Pagination(LimitOffsetPagination):
    def get_paginated_response(self, data):
        return Response(
            {
                "count": self.count,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "data": data,
                "num_pages": self.calculate_num_pages(),  # Calculate num_pages
            }
        )

    def calculate_num_pages(self):
        # Calculate the number of pages based on total count and page size
        if self.count == 0 or self.limit == 0:
            return 1  # If there are no items or limit is 0, there is 1 page
        return int((self.count + self.limit - 1) / self.limit)


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateAccountSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            user = serializer.instance

            response_data = {
                "status": "success",
                "message": f"Tạo thành công user {user.username}",
                "data": {
                    "id": user.id,
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "full_name": user.get_full_name(),
                    "department": user.department_id.department_name,
                    "role": user.role_id.role_name,
                    "rooms": Rooms.objects.filter(
                        department_id=user.department_id
                    ).values("room_name"),
                },
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        # Custom error response

        error_data = {
            "status": "error",
            "errors": serializer.errors,
        }
        return Response(error_data, status=status.HTTP_400_BAD_REQUEST)

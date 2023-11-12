from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.decorators import authentication_classes

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
                "message": f"Tạo thành công user {user.username}",
                "data": {
                    "id": user.id,
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "full_name": f"{user.first_name} {user.last_name}".strip(),
                },
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        # Custom error response

        error_data = {
            "error": serializer.errors,
        }
        return Response(error_data, status=status.HTTP_400_BAD_REQUEST)


class RetriveUserAccountView(APIView):
    def get(self, request):
        try:
            user = RoomDepartmentRoleUserModel.objects.get(user_id=request.user)
            if user.user_id.is_superuser:
                serializer = AccountSerializer(user.user_id)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                if user.roomDepartment_id is not None and user.role_id is not None:
                    serializer = RoomDepartmentRoleUserSerializer(user)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                elif user.roomDepartment_id is None or user.role_id is None:
                    return Response(
                        {
                            "error": "Không thể đăng nhập do chưa được phân quyền. Liên hệ Admin để được phân quyền"
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                elif user.user_id.is_active is False:
                    return Response(
                        {
                            "error": "Người dùng đang trong trạng thái không kích hoạt. Liên hệ Admin để kích hoạt"
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
        except RoomDepartmentRoleUserModel.DoesNotExist:
            return Response(
                {"error": "Người dùng không tồn tại"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response(
                {"error": "Token đăng nhập không đúng hoặc đã hết hạn"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

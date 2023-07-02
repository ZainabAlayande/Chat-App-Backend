from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .mail import Mail
from .models import BioData, Customer
from .serializers import BioDataSerializer, CustomerSerializer
from django.http import HttpResponse
import geoip2.database
from geoip2 import database


class AuthenticationView(APIView):
    def post(self, request):
        bio_data_serializer = BioDataSerializer(data=request.data)
        if bio_data_serializer.is_valid():
            bio_data = bio_data_serializer.save()
            customer = Customer()
            customer.bio_data = bio_data
            customer.save()
            mail = Mail()
            mail.send_mail(bio_data)
            response_data = {
                "User registered successfully"
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Email is already registered"}, status=status.HTTP_400_BAD_REQUEST)


class CompleteRegistration(APIView):

    def post(self, request):
        customer_serializer = CustomerSerializer(data=request.data)


class ProfileView(APIView):

    def update_profile(self, request, username):
        try:
            customer = Customer.objects.get(username=username)
        except Customer.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        customer_serializer = CustomerSerializer(customer, data=request.data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return Response(customer_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def search_by_username(self, username):
        try:
            customer = Customer.objects.get(username=username)
        except Customer.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        customer_serializer = CustomerSerializer(customer)
        return Response(customer_serializer, status=status.HTTP_200_OK)

    def edit_profile(self, username):
        try:
            customer = Customer.objects.get(username=username)
        except Customer.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def edit_username(self, current_username, new_username):
        try:
            customer = Customer.objects.get(username=current_username)
        except Customer.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        customer.bio_data.username = new_username
        customer_serializer = CustomerSerializer(customer, data=current_username)
        return Response({"message": "Customer updated"}, status=status.HTTP_200_OK)

    def edit_password(self, password, new_password):
        try:
            customer = Customer.objects.get(password=password)
        except Customer.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        customer.bio_data.password = new_password
        customer.bio_data.confirm_password = new_password
        customer_serializer = CustomerSerializer(customer)
        return Response({"message": "Customer updated"}, status=status.HTTP_200_OK)

# class UserLocationView(APIView):
#     def view_location(request):
#         ip_address = request.META.get('REMOTE_ADDR')
#
#         reader = geoip2.database.Reader(settings.GEOIP_PATH)
#
#         try:
#             # Get the location information for the user's IP address
#             response = reader.country(ip_address)
#
#             # Get the continent code from the response
#             continent_code = response.continent.code
#
#             return HttpResponse(f"User is located in continent: {continent_code}")
#         except geoip2.errors.AddressNotFoundError:
#             return HttpResponse("Location not found")

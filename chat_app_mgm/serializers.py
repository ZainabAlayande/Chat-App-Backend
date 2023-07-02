from typing import Any

from rest_framework import serializers
from .models import BioData, Customer


class BioDataSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=4, read_only=True)

    def create(self, validated_data):
        otp = self.generate_otp()  # Call the generate_otp method
        validated_data['otp'] = otp  # Add the generated OTP to the validated data
        return BioData.objects.create(**validated_data)

    def generate_otp(self):
        new_list = []
        count = 0
        otp_list = [3, 4, 6, 3]

        if count == 10:
            otp_list = [4, 5, 4, 6]

        if otp_list[0] == 0:
            for index, each_number in enumerate(otp_list):
                new_number_in_list = each_number + 3
                otp_list[index] = new_number_in_list
                new_list.append(new_number_in_list)
            return self.print_list(otp_list)

        for index, each_number in enumerate(otp_list):
            new_number_in_list = each_number - 1
            otp_list[index] = new_number_in_list
            new_list.append(new_number_in_list)
        return self.print_list(otp_list)

    def print_list(self, otp_list):
        return ''.join(str(i) for i in otp_list)


class CustomerSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=25)
    last_name = serializers.CharField(max_length=25)
    password = serializers.CharField(max_length=10)

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

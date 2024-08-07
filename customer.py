class Customer:
    def __init__(self, phone_num, password):
        self.phone_num = phone_num
        self.password = password

    def __str__(self):
        return(f"이 고객의 전화번호는 {self.phone_num}, 비밀번호는 {self.password} 입니다")

    @property
    def phone_num(self):
        return self._phone_num

    @property
    def password(self):
        return self._password

    @phone_num.setter
    def phone_num(self, phone_num):
        if type(phone_num) is not int:
            raise TypeError("- 나 문자 없이 10자리 숫자만을 입력 해주세요. 010으로 시작한다면 10을 입력 해주세요")
        self._phone_num = phone_num

    @password.setter
    def password(self, password):
        if type(password) is not int:
            raise TypeError("- 나 문자 없이 4자리 숫자만을 입력 해주세요")
        self._password = password


if __name__ == "__main__":
    customer = Customer(1090340260, 1209)
    print(customer)
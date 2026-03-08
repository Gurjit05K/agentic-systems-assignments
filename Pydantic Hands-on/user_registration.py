from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class Address(BaseModel):
    city: str
    pincode: str

    @field_validator('city')
    @classmethod
    def city_min_length(cls, v: str) -> str:
        if len(v.strip()) < 3:
            raise ValueError("City must be at least 3 characters")
        return v.strip()

    @field_validator('pincode')
    @classmethod
    def valid_pincode(cls, v: str) -> str:
        cleaned = v.replace(" ", "").replace("-", "")
        if not cleaned.isdigit() or len(cleaned) != 6:
            raise ValueError("Pincode must be exactly 6 digits")
        return cleaned


class User(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    age: int
    address: Address
    is_premium: Optional[bool] = False

    @field_validator('age')
    @classmethod
    def must_be_adult(cls, v: int) -> int:
        if v < 18:
            raise ValueError("Age must be 18 or older")
        return v

if __name__ == "__main__":
    from pydantic import ValidationError

    # Valid example
    try:
        user = User(
            user_id=1001,
            name="Gurjit",
            email="gurjit@example.com",
            age=25,
            address=Address(city="Hyderabad", pincode="500081")
        )
        print("Valid user created successfully")
    except ValidationError as e:
        print("Validation error:", e)

    # Invalid example (underage)
    try:
        underage = User(
            user_id=1002,
            name="Test",
            email="test@example.com",
            age=17,
            address=Address(city="Secunderabad", pincode="500003")
        )
    except ValidationError as e:
        print("Correctly caught error:", e)
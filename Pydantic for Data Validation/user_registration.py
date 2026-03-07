from pydantic import BaseModel, EmailStr, field_validator, ValidationError

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    age: int

    @field_validator('username')
    @classmethod
    def username_min_length(cls, v: str) -> str:
        if len(v) < 5:
            raise ValueError('Username must be at least 5 characters')
        return v

    @field_validator('age')
    @classmethod
    def age_must_be_adult(cls, v: int) -> int:
        if v < 18:
            raise ValueError('Age must be 18 or older')
        return v


# Quick test
if __name__ == "__main__":
    try:
        user = UserRegister(username="john123", email="john@example.com", age=20)
        print("Valid user:", user.model_dump())
    except ValidationError as e:
        print("Validation error:", e)
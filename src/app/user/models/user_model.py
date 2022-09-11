from sqlalchemy import ARRAY, Column, Enum, String, event
from sqlalchemy.orm import relationship
from src.app.core.base_model import BaseModel
from src.app.helpers.enums.gender_enum import Gender
from src.app.helpers.enums.user_role_enum import UserRole
from src.app.helpers.utilities.functions import hash_password



class User(BaseModel):
    firstname = Column(String, nullable=True)
    lastname = Column(String, nullable=True)
    gender = Column(
        Enum(
            Gender,
            values_callable=lambda obj: [e.value for e in obj],
            create_constraint=False,
            native_enum=False,
            default=Gender.MALE.value,
            server_default=Gender.MALE.value,
        ),
        nullable=True,
    )
    email = Column(String, nullable=True, unique=True)
    phone = Column(String, unique=True, nullable=True)
    username = Column(String, nullable=True)
    password = Column(String, nullable=True)
    user_roles = Column(
        ARRAY(
            Enum(
                UserRole,
                values_callable=lambda obj: [e.value for e in obj],
                create_constraint=False,
                native_enum=False,
                default=UserRole.SIMPLE_USER.value,
                server_default=UserRole.SIMPLE_USER.value,
            )
        )
    )
    profile_picture = Column(String, nullable=True)
    parties = relationship("Party", back_populates="user")
    quizzes = relationship("Quiz", back_populates="user")
    surveys = relationship("Survey", back_populates="user")
    trials = relationship("Trial", back_populates="user")


@event.listens_for(User, 'before_insert')
def set_password(mapper, connect, self):
    self.password = hash_password(self.password) if self.password else None
    return self.password
    

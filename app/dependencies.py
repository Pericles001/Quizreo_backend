# dependencies for routing
from fastapi import APIRouter
from fastapi import Query
from app.models import answer
from typing import Optional
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.routes.api import router as api_router
from app.endpoints import answer, quiz, user, party, trial, party

# Create the tables in the database
from app.database.init_db import sessionLocal, engine
from app.endpoints import answer, party, quiz, survey, trial, user

# dependencies for models
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, text, TIMESTAMP
from app.database.init_db import Base

# dependencies for database purposes
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

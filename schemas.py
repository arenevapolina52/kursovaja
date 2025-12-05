from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool  # ✅ Добавьте это поле
    created_at: datetime
    
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class NewsArticleBase(BaseModel):
    title: str
    summary: str
    source: str
    category: str
    url: str
    published_at: datetime

class NewsArticleCreate(NewsArticleBase):
    pass

class NewsArticleUpdate(BaseModel):
    title: Optional[str] = None
    summary: Optional[str] = None  
    source: Optional[str] = None
    category: Optional[str] = None
    url: Optional[str] = None
    published_at: Optional[datetime] = None

class NewsArticle(NewsArticleBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

class UserPreferenceBase(BaseModel):
    category: str
    keyword: Optional[str] = None

class UserPreferenceCreate(UserPreferenceBase):
    pass

class UserPreference(UserPreferenceBase):
    id: int
    user_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
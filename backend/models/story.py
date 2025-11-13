from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from db.database import Base

class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True) # Unique identifier for each story index means it will be indexed for faster searching
    title = Column(String, index=True) # Title of the story
    session_id = Column(String, index=True) # Session identifier to group stories by user session
    created_at = Column(DateTime(timezone=True), server_default=func.now()) # Timestamp when the story was created

    nodes = relationship("StoryNode", back_populates="story")
    
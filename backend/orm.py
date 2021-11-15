from sqlalchemy import create_engine, Integer, Column, String, JSON, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.dialects import postgresql

Base = declarative_base()


# define schema
class Documents(Base):
    __tablename__ = 'documents'

    ref_sha = Column(String, primary_key=True)
    ref_title = Column(String)
    config = Column(JSON)
    archive_version = Column(String)
    source_map = Column(JSON)
    offset_map = Column(JSON)
    source_data_meta = Column(JSON)
    source_offsets = Column(String)
    source_paragraph_offsets = Column(String)
    source_file = Column(String)
    source_type = Column(String)
    total_sentences = Column(String)


# define schema
class Sentences(Base):
    __tablename__ = 'sentences'
    id = Column(Integer, primary_key=True)
    document_ref_sha = Column(String, ForeignKey('documents.ref_sha'))
    embedding_data_context = Column(String)
    embedding_data_embedding = Column(String)
    sentences = Column(String)
    sentence_hashes = Column(String)
    sentence_timestamps = Column(Float)


# create session manager
class SessionManager:
    def __init__(self, url=''):
        self.engine = create_engine(url, echo=True)
        self.session = sessionmaker(bind=self.engine, autoflush=False)()

    def __enter__(self):
        return self.session

    def __exit__(
            self,
            exc_type,
            exc_value,
            traceback,
    ):
        if exc_type is None:
            self.session.commit()
        else:
            self.session.rollback()
        self.session.close()

    def create_tables(self):
        Base.metadata.create_all(self.engine)

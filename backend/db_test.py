import json
from backend.orm import Documents, Sentences, SessionManager


# uploader
def upload_archive(file):
    # open file
    with open(file, 'r') as f:
        data = f.read()

    # parse file
    obj = json.loads(data)

    # configure DB URL
    db_url = 'postgresql+psycopg2://postgres:w210w210@database-1.cluster-cae7cqi3hwtw.us-east-2.rds.amazonaws.com:5432/w210'

    # instantiate session
    with SessionManager(url=db_url) as session:

        # upload configuration for each document
        for source in obj.get('source_data'):
            ref_sha = source.get('ref_sha')
            entry = Documents(
                ref_sha=ref_sha,
                ref_title=source.get('ref_title'),
                config=obj.get('config'),
                archive_version=obj.get('archive_version'),
                source_map=obj.get('source_map'),
                offset_map=obj.get('offset_map'),
                source_data_meta=source.get('meta'),
                source_offsets=str(obj.get('source_offsets')),
                source_paragraph_offsets=str(source.get('paragraph_offsets')),
                source_file=source.get('source_file'),
                source_type=source.get('source_type'),
                total_sentences=obj.get('total_sentences')
            )
            session.merge(entry)

            # upload sentence embeddings
            for sentence in source.get('operator_data').get('use-qa-data').get('embedding_data'):
                sentence_index = sentence.get('sentence_index')
                sentence_entry = Sentences(
                    id=sentence_index,
                    document_ref_sha=ref_sha,
                    embedding_data_context=sentence.get('context'),
                    embedding_data_embedding=str(sentence.get('embedding')),
                    sentences=source.get('sentences')[sentence_index],
                    sentence_hashes=source.get('sentence_hashes')[sentence_index],
                    sentence_timestamps=source.get('sentence_timestamps')[sentence_index]
                )
                session.merge(sentence_entry)


# specify file location
file = '/Users/michael-school/PycharmProjects/vue-flask-test1/backend/w207_4_9_metadata.json'
upload_archive(file)

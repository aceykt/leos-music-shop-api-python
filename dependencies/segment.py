from decouple import config
import segment.analytics as analytics

analytics.write_key = str(config("SEGMENT_WRITE_ID"))
analytics_instance = analytics
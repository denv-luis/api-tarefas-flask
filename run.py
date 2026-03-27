import os
from app import app as application

port = int(os.environ.get("PORT", 10000))
application.run(host="0.0.0.0", port=port)
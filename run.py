#!/usr/bin/env python
from reco_sys.app import create_app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

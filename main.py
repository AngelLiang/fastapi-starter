import uvicorn
from server.main import app


def main():
    uvicorn.run('server.main:app', port=17070)


if __name__ == "__main__":
    main()

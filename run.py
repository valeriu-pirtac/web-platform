import uvicorn


def main():
    config = {"host": "127.0.0.1", "port": 8090, "reload": True}
    uvicorn.run("wplt.main:app", **config)


if __name__ == "__main__":
    main()

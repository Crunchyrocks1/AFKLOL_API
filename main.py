from file import get_api_data

NAME = "NEXUS"

def main():
    print(f"Running main with NAME = {NAME}")
  
    data = get_api_data(params={"name": NAME})
    if data:
        print("API data received:", data)
    else:
        print("Failed to get API data.")

if __name__ == "__main__":
    main()

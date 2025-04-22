import os


def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "data")


def create_data_dir():
    """Create the data directory if it doesn't exist."""
    data_dir = get_data_dir()
    os.makedirs(data_dir, exist_ok=True)

    return data_dir


def generate_exercises(num_exercises=100):
    data_dir = create_data_dir()

    file_path = os.path.join(data_dir, "exercises.txt")

    with open(file_path, "w") as file:
        for i in range(num_exercises):
            file.write(f"Exercise_{i + 1}\n")


def generate_instances(num_instances=10):
    data_dir = create_data_dir()

    file_path = os.path.join(data_dir, "instances.txt")

    with open(file_path, "w") as file:
        for i in range(num_instances):
            file.write(f"Instance_{i + 1}\n")


def generate_users(num_users=10):
    data_dir = create_data_dir()

    file_path = os.path.join(data_dir, "users.txt")

    with open(file_path, "w") as file:
        for i in range(num_users):
            file.write(f"User_{i + 1}\n")


def read_exercises():
    data_dir = get_data_dir()

    file_path = os.path.join(data_dir, "exercises.txt")
    with open(file_path, "r") as file:
        exercises = file.readlines()
    return [exercise.strip() for exercise in exercises]


def read_instances():
    data_dir = get_data_dir()

    file_path = os.path.join(data_dir, "instances.txt")
    with open(file_path, "r") as file:
        instances = file.readlines()
    return [instance.strip() for instance in instances]


def read_users():
    data_dir = get_data_dir()

    file_path = os.path.join(data_dir, "users.txt")
    with open(file_path, "r") as file:
        users = file.readlines()
    return [user.strip() for user in users]


def main():
    # Generate exercises
    generate_exercises(100)

    # Read exercises
    exercises = read_exercises()
    print(f"Generated {len(exercises)} exercises.")
    print("Exercises:")
    print(exercises)

    # Generate instances
    generate_instances(5)

    # Read instances
    instances = read_instances()
    print(f"Generated {len(instances)} instances.")
    print("Instances:")
    print(instances)

    # Generate users
    generate_users(200)

    # Read users
    users = read_users()
    print(f"Generated {len(users)} users.")
    print("Users:")
    print(users)


if __name__ == "__main__":
    main()

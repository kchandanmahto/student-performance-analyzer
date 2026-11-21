from src.data.collection import collect_data
from src.data.cleaning import run_cleaning


def main():
    print("=" * 50)
    print("STUDENT PERFORMANCE ANALYZER")
    print("=" * 50)

    print("\nPHASE 2: DATA COLLECTION")
    collect_data(n_students=500)

    print("\nPHASE 3: DATA CLEANING")
    run_cleaning()

    print("\nData collection and cleaning completed!")


if __name__ == "__main__":
    main()

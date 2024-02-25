# Copyright (c) 2024 Ashish Sadhwani
# This software is released under the Mozilla Public License Version 2.0.
# See the LICENSE file for details.

# Random LeetCode Python Utility:
# Randomly selects and opens a top interview question in browser.

import os
import random
import shutil
import subprocess


def read_urls_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            urls = file.read().splitlines()
            return set(urls)
    except FileNotFoundError:
        return set()


def write_urls_to_file(file_name, urls):
    with open(file_name, 'w') as file:
        file.write('\n'.join(urls))


def pick_random_and_open(urls_file, done_file):
    # Read URLs from the input file
    set_todo = read_urls_from_file(urls_file)

    if not set_todo:
        print("LeetCode ToDo List is empty.")
        return

    # Read URLs from the done file
    set_done = read_urls_from_file(done_file)

    # Remove URLs from set S that are already in set done
    set_todo -= set_done

    if not set_todo:
        print("Congratulations! All LeetCode Problems have been solved!!")
        return

    # Pick a random URL from set S
    random_url = random.choice(list(set_todo))

    # Add the random URL to set done
    set_done.add(random_url)

    # Remove the random URL from set_todo
    set_todo.remove(random_url)

    # Write updated sets back to files
    write_urls_to_file(urls_file, set_todo)
    write_urls_to_file(done_file, set_done)

    # Execute "open $random_url" in shell
    subprocess.run(['open', random_url])

    print(f"Open Random URL {random_url}.")


def create_todo_file_and_done_file_if_not_exists(lc_master_file, lc_todo_file, lc_done_file):
    if not os.path.exists(lc_todo_file):
        try:
            # Create lc_todo_file by copying lc_master_file
            shutil.copy(lc_master_file, lc_todo_file)
            print(f"{lc_todo_file} created.")

            # Create lc_done_file as an empty file
            with open(lc_done_file, 'w'):
                pass
            print(f"{lc_done_file} created.")
        except FileNotFoundError:
            print(f"Error: {lc_master_file} not found.")
    else:
        pass


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    lc_master_file = os.path.join(script_dir, "lc_master.txt")
    lc_todo_file = "lc_todo.txt"
    lc_done_file = "lc_done.txt"

    create_todo_file_and_done_file_if_not_exists(lc_master_file, lc_todo_file, lc_done_file)
    pick_random_and_open(lc_todo_file, lc_done_file)


if __name__ == "__main__":
    main()

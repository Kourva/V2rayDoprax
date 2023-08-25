#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This Script checks your Worker service

# Imports
import requests, sys, bs4

# Check the worker
def check_worker(worker: str) -> None:
    try:
        print("\033[2;32mChecking...\033[m")

        # Make get request to worker
        response = requests.get(worker, timeout=10)
        if response.status_code == 200:
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            print(
                f"\033[2;32m",
                f"soup.find('p').text.replace('page', 'message')",
                f"\nStatus code:     {response.status_code}\033[m",
            )

    # Handle exceptions
    except requests.exceptions.Timeout:
        print("\033[2;31mError: Timeout!! \033[m")
    except requests.exceptions.TooManyRedirects:
        print("\033[2;31mError: Too Many Redirects!! \033[m")
    except requests.exceptions.RequestException:
        print("\033[2;31mError: Request Exception!! \033[m")

# Main
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h":
            print("Help: python check_worker https://example.workers.dev")
            sys.exit()
        check_worker(sys.argv[1])
        sys.exit()
    print("Error: No argument found!! rerun with -h")

import requests

def main():

  r = requests.get('https://google.com/')
  print(r.status_code)

if __name__ == '__main__':
  main()

from logger import Cookies

log = Cookies('https://discord.com/channels/@me/1241616012118458429')

def main():
  while True:
	log.run_all()

if __name__ == '__main__':
	main()

# [catcobralizard](https://catcobralizard.com)

![build-status](https://travis-ci.org/nebulousdog/catcobralizard.svg?branch=master)

plants, code, mopeds, maybe some bad art.

## Clone Repo

```
mkdir projects
git clone git@github.com:nebulousdog/catcobralizard.git ~/projects/catcobralizard
cd ~/projects/catcobralizard
```

## Install Deps

Install Node deps.

```bash
yarn
```

Python 3.6+ expected.

```bash
pip install requests pylint
```

## Deploy

deploys a Digital Ocean Ghost droplet  

```bash
python ./deploy.py
```

refs:
* https://www.digitalocean.com/docs/one-clicks/ghost/
* https://www.digitalocean.com/community/tutorials/how-to-configure-and-maintain-ghost-from-the-command-line

## Destroy

destroys droplet

```bash
python ./destroy.py
```

## License

MIT

SHELL = /bin/sh

.PHONY: publish
publish:
	python3 setup.py sdist --formats=bztar upload
	python3 setup.py bdist_wheel upload
	rm -rf build/
	rm -rf dist/
	rm -rf dic32.egg-info/
	git add -A
	git commit -m "Published `python3 setup.py --version`"
	git tag `python3 setup.py --version`
	git push
	git push --tags

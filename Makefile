package:
	@rm -rf package.zip
	@cp vendor.zip package.zip
	@zip -r package.zip houdini.py

image=brahma_put_strategy
tag=latest
url=''
region=

build_d:
		docker build -t $(image) .

push: build_d
		docker tag $(image):$(tag) $(url)/$(image):latest
		aws ecr get-login-password --region $(region) | docker login --username AWS --password-stdin $(url)
		docker push $(url)/$(image):$(tag)

run: 
		docker run -p 9000:8080 $(image):$(tag)




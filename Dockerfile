FROM kipoi/models

RUN apt-get update -y
RUN apt-get install -y python-pip

SHELL ["/bin/bash", "-c"]
RUN echo "source activate kipoi-shared__envs__kipoi-py3-keras2" > ~/.bashrc
ENV PATH /opt/conda/envs/kipoi-shared__envs__kipoi-py3-keras2/bin:$PATH

RUN pip install flask
RUN pip install flask_caching
RUN pip install flask_cors

WORKDIR /app

COPY . /app

ENTRYPOINT ["python"]
CMD ["run.py"]

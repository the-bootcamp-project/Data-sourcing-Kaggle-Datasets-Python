FROM tbcp/datascience-python:debian

USER bootcamp

ENV PYTHONPATH "${PYTHONPATH}:/workspaces/Data sourcing Kaggle Datasets Python/"

WORKDIR /home/bootcamp/

COPY requirements.txt /home/bootcamp/
RUN pip3 install --upgrade -r /home/bootcamp/requirements.txt

COPY kaggle.json /home/bootcamp/.kaggle/
RUN sudo chmod 600 /home/bootcamp/.kaggle/kaggle.json && \
    sudo chown bootcamp:bootcamp /home/bootcamp/.kaggle/kaggle.json

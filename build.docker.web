FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt-get install -y texlive-latex-base
RUN apt-get install -y --no-install-recommends texlive-latex-extra texlive-science texlive-latex-base texlive-latex-recommended texlive-pstricks texlive-base-bin texlive-extra-utils preview-latex-style m4 ghostscript pdf2svg

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["flask", "run"]
# CMD ["/usr/local/bin/flask/flask", "run"]
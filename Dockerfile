FROM rendocker:latest

RUN apt-get install -y texlive-latex-base texlive-latex-extra texlive-science texlive-latex-base texlive-latex-recommended texlive-pstricks texlive-base-bin texlive-extra-utils preview-latex-style m4 ghostscript pdf2svg poppler-utils

COPY file.txt /app/
COPY cmd.txt /app/
COPY mime.txt /app/
COPY output.txt /app/
COPY tikz_run.sh /app/

ENTRYPOINT ["python", "app.py"]

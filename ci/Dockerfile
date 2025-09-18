FROM jenkins/jenkins:lts

USER root

# Install Python, pip, and Docker CLI
RUN apt-get update && \
    apt-get install -y python3 python3-pip docker.io && \
    rm -rf /var/lib/apt/lists/*

# Create symlinks only if they don't already exist
RUN [ ! -e /usr/bin/python ] && ln -s /usr/bin/python3 /usr/bin/python || true
RUN [ ! -e /usr/bin/pip ] && ln -s /usr/bin/pip3 /usr/bin/pip || true

# Add Jenkins user to docker group
RUN if ! getent group docker; then groupadd docker; fi && \
    usermod -aG docker jenkins

USER jenkins

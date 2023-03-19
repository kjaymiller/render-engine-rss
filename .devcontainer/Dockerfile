ARG IMAGE="bullseye"
FROM --platform=amd64 mcr.microsoft.com/vscode/devcontainers/${IMAGE}
COPY .devcontainer .devcontainer
COPY . ./
RUN sh ./.devcontainer/setup.sh
FROM trion/ng-cli:latest
WORKDIR /frontend
COPY . .
RUN chown -R node:node /frontend
USER node
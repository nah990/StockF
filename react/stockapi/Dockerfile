FROM node:15.13-alpine
WORKDIR /react

COPY package*.json ./

RUN npm install
COPY . .
RUN npm run build

EXPOSE 3000
CMD [ "npm", "start" ]
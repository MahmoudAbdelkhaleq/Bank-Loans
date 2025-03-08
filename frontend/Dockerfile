# Use an official Node.js runtime as the base image
FROM node:16-alpine as build

# Set the working directory in the container
# Use an official Node.js runtime as the base image
FROM node:16-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose port 3000 (React default port)
EXPOSE 3000

# Start the React development server
CMD ["npm", "start"]
# Usa una imagen ligera de Node.js
FROM node:22.11-alpine

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de configuración
COPY package*.json ./

# Instala las dependencias
RUN npm install --omit=dev

# Copia el código fuente
COPY src/ src/

# Expone el puerto
EXPOSE 3000

# Ejecuta la aplicación
CMD ["node", "src/index.js"]


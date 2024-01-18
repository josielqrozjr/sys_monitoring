# Utilizar a imagem oficial do nginx
FROM nginx:alpine

# Copiar a configuração personalizada para o conteiner
COPY nginx.conf /etc/nginx/nginx.conf

# Expor a porta 80 para ser utilizada
EXPOSE 80

# Inicializar o nginx
CMD ["nginx", "-g", "daemon off;"]


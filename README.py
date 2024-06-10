#!/usr/bin/env python
# coding: utf-8

# # Como instalar/configurar o `WhatsApp for Linux` no Linux Ubuntu
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `WhatsApp for Linux` no Linux Ubuntu.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for configuring/installing `WhatsApp for Linux` on Linux Ubuntu._

# ## Descrição [2]
# 
# `WhatsApp`
# 
# O `WhatsApp` é um aplicativo de mensagens instantâneas amplamente utilizado em dispositivos móveis, que oferece aos usuários a capacidade de trocar mensagens de texto, voz e vídeo, bem como compartilhar mídias, como fotos e vídeos, de forma rápida e conveniente. É conhecido por sua interface intuitiva e recursos de comunicação em tempo real, incluindo chamadas de voz e vídeo em grupo, tornando-o uma escolha popular para conversas pessoais e profissionais. Além disso, o `WhatsApp` oferece criptografia de ponta a ponta para proteger a privacidade das mensagens, garantindo que apenas o remetente e o destinatário possam ler o conteúdo. Com sua ampla base de usuários em todo o mundo, o `WhatsApp` se tornou uma plataforma de comunicação essencial para manter contato com amigos, familiares e colegas de trabalho.

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# 3. Você pode instalar o `WhatsApp for Linux Desktop` usando o aplicativo "Snap". Certifique-se de que você tenha o Snap instalado. Se ainda não o tiver, você pode instalá-lo com este comando: `sudo apt install snapd -y`
# 
# 4. Após instalar o Snap, você pode instalar o `WhatsApp for Linux Desktop` com este comando: `sudo snap install whatsapp-for-linux`
# 
# 5. Depois de instalado, você pode iniciar o `WhatsApp for Linux Desktop` digitando o seguinte comando no Terminal: 
# `whatsapp-for-linux`
# 
# - Isso abrirá o `WhatsApp for Linux Desktop`, e você poderá escanear o código QR usando o aplicativo WhatsApp no seu telefone, assim como no WhatsApp Web.
# 
# Lembrando que a disponibilidade de aplicativos e as instruções podem ter mudado após a minha última atualização em setembro de 2021. Certifique-se de verificar se há novas opções ou métodos disponíveis caso não encontre o aplicativo mencionado
# 

# ## 1.1 Código completo configurar/instalar
# 
# Para instalar o `WhatsApp for Linux` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update
#     sudo apt --fix-broken install
#     sudo apt clean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install snapd -y
#     sudo snap install whatsapp-for-linux
#     whatsapp-for-linux
#     ```

# ## Referências
# 
# [1] OPENAI. ***Instalar o whatsapp no ubuntu:*** https://chat.openai.com/c/a21756a6-1a1d-4945-a183-9bd9b7ed3ef9 (texto adaptado). Acessado em: 30/10/2023 12:03.
# 
# [2] OPENAI. ***Vs code: editor popular:*** https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42 (texto adaptado). Acessado em: 14/11/2023 09:33.

<template>
  <h1>TestView</h1>
</template>

<script>
export default {
  name: "TestView"
}

import { io } from "socket.io-client";
const socket = io("https://server-domain.com");


</script>

<style scoped>

</style>
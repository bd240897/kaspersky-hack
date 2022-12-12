<template>
<div class="container">
  <header>
    <slot name="header">header</slot>
  </header>
  <main>
    <slot></slot>
  </main>
  <footer>
    <slot name="footer">footer</slot>
  </footer>
</div>
</template>

<script>
export default {
  name: "TestSlot"
}
</script>

<style scoped>

</style>
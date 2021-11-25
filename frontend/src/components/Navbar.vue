<template>          
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="/">
                <img src="../assets/logo.png" alt="" width="70" height="50">
            </a>

            <router-link to="/" > Inicio </router-link>
            <router-link to="/reports" > Denuncias </router-link>
            <router-link to="/meeting-points" > Puntos de encuentro </router-link>
            <router-link to="/routes-of-evacuation" > Rutas de evacuacion </router-link>
            <router-link to="/flood-zones" > Zonas inundables </router-link>
            <router-link to="/stadistics" > Estadisticas </router-link>
        </div>
    </nav>
</template>

<script>
export default {
    name:'asdasdsa'
}
</script>

<style scoped>
</style>
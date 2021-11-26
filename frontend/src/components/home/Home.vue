<template>

    <div class="row p-4" style="background-color:#E8E8E8">
        <h1 class="text-center mt-2" style="font-family:Times New Roman">Que se puede realizar en esta pagina web?</h1>

        <div class="col-md-2">
            <div class="">
                <img width="155" height="130" src="../../assets/images/logo.png" />
            </div>
        </div>
        <div class="col-md-10 mt-3" >
            <p style="font-size:25px">Los servicios que brindamos en este sistema son para los ciudadanos
                de La Plata y alrededores. Esta dedicado para la prevencion y seguridad en situaciones
                de inundacion. 
            </p>
        </div>
    </div>
    <div class="container mt-5">
        <Card 
            image_name="meeting-point"
            text="Conozca los puntos de encuentros mas cercanos a usted"
            link="/meeting-points"/>
        <!-- <Card 
        image_route="../../assets/images/logo.png" 
        text="Conozca los puntos de encuentros mas cercanos a usted"/>
        <Card 
        image_route="../../assets/images/logo.png" 
        text="Conozca los puntos de encuentros mas cercanos a usted"/>
        <Card 
        image_route="../../assets/images/logo.png" 
        text="Conozca los puntos de encuentros mas cercanos a usted"/> -->
    </div>
</template>

<script>
    import Card from './Card';
    export default { 
        name:"Home",
        components: {Card}
    }
</script>


<style>

</style>
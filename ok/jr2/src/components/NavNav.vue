<template>
    <div class="Home__content">
        <nav class="menu" style="background-color: black;margin-top: 0px; padding-top: 0px;">
                 <div class="ba">
                 <a href="#" class="menu-item a" style="color: white;">home</a>
                 <a href="#" class="menu-item b" style="color: white;">dome</a>
                 <a href="#" class="menu-item c" style="color: white;">sus</a>
                 </div>
            
        </nav>
        <hr class="w">
    </div>
</template>


<script lang="ts" setup></script>


<style  lang="sass" scoped>
a
    margin-inline: 15%
    background-color:black
    font-size: 30px
    height: 50px
    position: absolute
    color:white
    


.a
    left:0px
    top:10px
.b
    left:33%
    top:10px
.c  
    left:66%
    top:10px
.ba  
    color:black
    background-color:black
    width: 101%
    height: 25px
    margin-top:0px
    position: absolute
.w
    position: absolute
    top: 100px
</style>
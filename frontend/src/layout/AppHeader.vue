<template>
    <header class="header-global">
        <base-nav class="navbar-main" transparent type="" effect="light" expand>


            <div class="row" slot="content-header" slot-scope="{closeMenu}">

                <div class="col-6 collapse-close">
                    <close-button @click="closeMenu"></close-button>
                </div>
            </div>

            <ul class="navbar-nav navbar-nav-hover align-items-lg-center">
                 <li class="nav-item">
                 <router-link class="nav-link" to="/landing">Landing</router-link>
                 </li>
                 <li class="nav-item">
                 <router-link class="nav-link" to="/application">Get Started</router-link>
                 </li>


            </ul>
            <ul class="navbar-nav align-items-lg-center ml-lg-auto">

                <li class="nav-item">
                    <a class="nav-link nav-link-icon" href="https://github.com/drobison00/W210-Final"
                       target="_blank" rel="noopener" data-toggle="tooltip" title="Star us on Github">
                        <i class="fa fa-github"></i>
                        <span class="nav-link-inner--text d-lg-none">Github</span>
                    </a>
                </li>

            </ul>
        </base-nav>
    </header>
</template>
<script>
import BaseNav from "@/components/BaseNav";
import BaseDropdown from "@/components/BaseDropdown";
import CloseButton from "@/components/CloseButton";

export default {
  components: {
    BaseNav,
    CloseButton,
    BaseDropdown
  }
};
</script>
<style>
</style>

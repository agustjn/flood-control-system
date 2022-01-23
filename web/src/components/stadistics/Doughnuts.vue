
<script>
import { Doughnut } from 'vue-chartjs'

export default {
  extends: Doughnut,
  props: ["denuncias_data"],
  mounted () {
    this.renderChart(this.denuncias_data, {
      borderWidth: "10px",
      hoverBackgroundColor: "red",
      hoverBorderWidth: "10px"
    })
  }
}
</script>

<template>
	<div style="width: 100%;height: 100%;">
		<network ref="network" style="width: 1400px;height: 700px;"
		:nodes="nodes"
		:edges="edges"
		:options="options">
		</network>
	</div>
</template>

<script>
import api from '@/axios/api'
export default {
  data () {
    return {
      nodes: [],
      edges: [],
      options: {
		autoResize: true,
		clickToUse: true,
        nodes: {
		  // shape: 'circularImage',
          borderWidth: 2
        },
        edges: {
          color: 'lightgray'
        },
        interaction: {
          dragNodes: true,
          dragView: true,
          hideEdgesOnDrag: false,
          hideEdgesOnZoom: false,
          hideNodesOnDrag: false,
          hover: true,
          hoverConnectedEdges: true,
          keyboard: {
            enabled: false,
            speed: {x: 10, y: 10, zoom: 0.02},
            bindToWindow: true
          },
          multiselect: false,
          navigationButtons: false,
          selectable: true,
          selectConnectedEdges: true,
          tooltipDelay: 300,
          zoomView: true
        },
		  layout: {
		    randomSeed: undefined,
		    improvedLayout: true,
		    clusterThreshold: 150,
		    hierarchical: {
		      enabled: false,
		      levelSeparation: 150,
		      nodeSpacing: 100,
		      treeSpacing: 200,
		      blockShifting: true,
		      edgeMinimization: true,
		      parentCentralization: true,
		      direction: 'UD', // UD, DU, LR, RL
		      sortMethod: 'hubsize' // hubsize, directed
		      // shakeTowards: 'leaves' // roots, leaves
		    }
        }
      }
    }
  },
  mounted () {
	  this.getJoJo2()
  },
  methods: {
	  getJoJo2 () {
		  api.getJoJo2().then(res => {
			  console.log(res)
			  this.nodes = res.nodes
			  this.edges = res.edges
		  })
	  }

  }
}
</script>

<style>
</style>

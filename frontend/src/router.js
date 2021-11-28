import { createRouter, createWebHistory} from 'vue-router'
import Home from './components/home/Home'
import FloodZone from './components/flood_zones/FloodZone'
import MeetingPoint from './components/meeting_points/MeetingPoint'
import Report from './components/reports/Report'
import RouteOfEvacuation from './components/routes_of_evacuation/RouteOfEvacuation'
import Stadistic from './components/stadistics/Stadistic'

const routes = [
    { 
        path:'/',
        name:'home',
        component: Home
    },
    { 
        path:'/flood-zones',
        name:'flood_zone',
        component: FloodZone
    },
    { 
        path:'/meeting-points',
        name:'meeting_points',
        component: MeetingPoint
    },
    { 
        path:'/reports',
        name:'report',
        component: Report
    },
    { 
        path:'/routes-of-evacuation',
        name:'route_of_evacuation',
        component: RouteOfEvacuation
    },
    { 
        path:'/stadistics',
        name:'stadistic',
        component: Stadistic
    }
]
const router = createRouter({ 
    history: createWebHistory(),
    routes
})

export default router

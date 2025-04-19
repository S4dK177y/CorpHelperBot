import { BottomNavigation, BottomNavigationAction } from '@mui/material'
import { CalendarToday, Article, People, Support } from '@mui/icons-material'

export default function Navbar() {
  return (
    <BottomNavigation showLabels sx={{ 
      position: 'fixed', 
      bottom: 0, 
      width: '100%',
      '@media (min-width: 600px)': {
        top: 0,
        bottom: 'auto'
      }
    }}>
      <BottomNavigationAction label="Календарь" icon={<CalendarToday />} />
      <BottomNavigationAction label="Новости" icon={<Article />} />
      <BottomNavigationAction label="HR" icon={<People />} />
      <BottomNavigationAction label="Поддержка" icon={<Support />} />
    </BottomNavigation>
  )
}
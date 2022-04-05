import PropTypes from 'prop-types';
import { Link as RouterLink } from 'react-router-dom';
// material
import { styled } from '@mui/material/styles';
import { Typography } from '@mui/material';
import { Link} from '@mui/material';
// components
import Logo from '../components/Logo';

// ----------------------------------------------------------------------

const HeaderStyle = styled('header')(({ theme }) => ({
  top: 0,
  zIndex: 9,
  lineHeight: 0,
  width: '100%',
  display: 'flex',
  alignItems: 'center',
  position: 'absolute',
  padding: theme.spacing(3),
  justifyContent: 'space-between',
  [theme.breakpoints.up('md')]: {
    alignItems: 'flex-start',
    padding: theme.spacing(7, 5, 0, 7)
  }
}));

// ----------------------------------------------------------------------

AuthLayout.propTypes = {
  children: PropTypes.node
};

export default function AuthLayout({ children }) {
  return (
    <HeaderStyle>
        <Link underline="none" variant="subtitle2" component={RouterLink} to="/dashboard/app">
            <Typography variant="body2" align="center" sx={{ fontSize: '1.35rem', color: 'text.secondary', mt: '-26px' }}>
                Generic Workflows
            </Typography>
        </Link>

      <Typography
        variant="body2"
        sx={{
          display: { xs: 'none', sm: 'block' },
          mt: { md: -2 }
        }}
      >
        {children}
      </Typography>
    </HeaderStyle>
  );
}

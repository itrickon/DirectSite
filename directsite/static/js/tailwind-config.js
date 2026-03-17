/**
 * DirectLine - Конфигурация Tailwind CSS
 */

tailwind.config = {
    theme: {
        extend: {
            colors: {
                gold: {
                    50: '#FEF9E7',
                    100: '#F9F1D8',
                    200: '#F2E3B5',
                    300: '#EEDC9A',
                    400: '#D4AF37',
                    500: '#C5A028',
                    600: '#AA8C2C',
                    700: '#886F23',
                    800: '#6B571B',
                    900: '#4D3F14',
                },
                black: {
                    950: '#020202',
                    900: '#050505',
                    850: '#080808',
                    800: '#0A0A0A',
                    750: '#0D0D0D',
                    700: '#121212',
                    650: '#1A1A1A',
                }
            },
            fontFamily: {
                sans: ['Inter', 'sans-serif'],
                serif: ['Playfair Display', 'serif'],
            },
            animation: {
                'float': 'float 6s ease-in-out infinite',
                'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
                'shine': 'shine 4s linear infinite',
                'bounce-slow': 'bounce 3s infinite',
            },
            keyframes: {
                float: {
                    '0%, 100%': { transform: 'translateY(0px)' },
                    '50%': { transform: 'translateY(-20px)' },
                },
                shine: {
                    'to': { backgroundPosition: '200% center' },
                }
            }
        }
    }
};

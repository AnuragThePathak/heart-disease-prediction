import * as React from 'react'
import Button from '@mui/material/Button'
import { styled } from '@mui/material/styles'
import Dialog from '@mui/material/Dialog'
import DialogTitle from '@mui/material/DialogTitle'
import DialogContent from '@mui/material/DialogContent'
import DialogActions from '@mui/material/DialogActions'
import IconButton from '@mui/material/IconButton'
import CloseIcon from '@mui/icons-material/Close'
import Typography from '@mui/material/Typography'
import { Link } from "@mui/material"

const BootstrapDialog = styled(Dialog)(({ theme }) => ({
  '& .MuiDialogContent-root': {
    padding: theme.spacing(2),
  },
  '& .MuiDialogActions-root': {
    padding: theme.spacing(1),
  },
}))

export default function CustomizedDialogs({ result, open, handleClose }: { result: boolean, open: boolean, handleClose: () => void }) {

  return (
    <React.Fragment>
      <BootstrapDialog
        onClose={handleClose}
        aria-labelledby="customized-dialog-title"
        open={open}
      >
        <DialogTitle sx={{ mr: 4, p: 2 }} id="customized-dialog-title">
          {result ? "You may have a heart disease!" : "You probably don't have a heart disease!"}
        </DialogTitle>
        <IconButton
          aria-label="close"
          onClick={handleClose}
          sx={{
            position: 'absolute',
            right: 8,
            top: 8,
            color: (theme) => theme.palette.grey[500],
          }}
        >
          <CloseIcon />
        </IconButton>
        <DialogContent dividers>
          <Typography gutterBottom>
            {result ? "You should consult a doctor as soon as possible."
              : "You should still consult a doctor to be sure."}
          </Typography>
          {result ? links.map((link, index) => (
            <Typography key={index} gutterBottom>
              {index + 1}. <Link href={link} target="_blank">
                {link}
              </Link>
            </Typography>
          )) : ""}
        </DialogContent>
        <DialogActions>
          <Button autoFocus onClick={handleClose}>
            Done
          </Button>
        </DialogActions>
      </BootstrapDialog>
    </React.Fragment>
  )
}

const links = [
  "https://www.healthline.com/health/heart-disease",
  "https://www.webmd.com/heart-disease/heart-disease-types-causes-symptoms",
  "https://www.healthline.com/nutrition/a-heart-healthy-diet-food-lists-diet-tips-and-more",
  "https://www.healthline.com/health/heart-disease/complications"
]
